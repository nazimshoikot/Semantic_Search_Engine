import './App.css';
import logo from './azeus_logo.jpg';
import { Form, Button, Spinner } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from "axios";
import React, { useState } from 'react';
var path = require('path');

function App() {
  /* 
  @query  Used to store the value of the query from the user
  @results  Used to store the results from the backend, empty initially
  @timeTaken stores the time taken for query from the backend
  @pageNum stored the current pageNum
  @hideSearchSpinner used to decide if the spinner should be shown during search
  @showResults used to toggle when to show results
  */
  const [query, setQuery]= useState('');
  const [results, setResults] = useState([]);
  const [timeTaken, setTimeTaken] = useState(-1);
  const [pageNum, setPageNum] = useState(1);
  const [hideSearchSpinner, setHideSpinner] = useState(true);
  const [showResults, setShowResults] = useState(false);

  // we are showing 100 results
  const RESULTS_PER_PAGE = 10;

  // used to store components that are later returned to page
  var resultsComponent = [];
  var timeComponent = null;
  var pagesArr = [];
  var totalPages = 0;


  /* Sends the query to the backend. Upon receipt of the names of the 
  document names from backend, sets the results so that the results can
  be rendered */
  function handleSearch(e) {
    e.preventDefault()

    // reset default values
    setShowResults(false);
    setHideSpinner(false);
    setPageNum(1);

    axios
      .get("http://localhost:8000/api/docs/?q="+query)
      .then(res => {
        let data = res.data;
        // extract time and results
        let time = data[0];
        let results = data[1];

        // set appropriate values from request
        setResults(results);
        setTimeTaken(time);
        
        // set appropriate flags
        setHideSpinner(true);
        setShowResults(true);

      }
      )
      .catch(err => {
        // if error found, hide the spinner 
        console.log(err);
        setHideSpinner(true); 
      })
  };

  // extracts the extension of the name given 
  // @name: full name of a document from which the extension is to be 
  //        derived
  // return: extension of the file
  function getExtension(name) {
    let nameArr = name.split('/')
    name = nameArr[nameArr.length-1]
    // console.log(name)
    let ext = path.basename(name).split('.');

    // if there is no extension (should not exist in current dataset)
    if (ext.length === 1) {
      ext  = "FILE"
    } else {
      ext = ext.pop()
    }

    ext = ext.toUpperCase();

    return ext
  }


  /*
  Renders the results after the search
  param: @result - the list of documents names returned from backend
  TODO: make the list empty during the time between a new query is 
        entered and the results for the new query is returned
        result[0] = doc_id
        result[1] = doc_name
        result[2] = preview
        result[3] = filepath
        result[4] = cosine_score
  */
  // console.log(results)
  if (showResults) {
    // decide which of the 100 results to show in current page
    let starting_index = (pageNum - 1) * RESULTS_PER_PAGE;
    let ending_index = starting_index + RESULTS_PER_PAGE;
    
    // add the results to the result components
    for (let i = starting_index; i < ending_index; i++) {
      let result = results[i];
      // console.log(result[3])
      let ext = getExtension(result[3])
      let fullname = result[1] + " [" + ext + "] "
      
      let resultComponent = (
      <div className="result-container" key={result[0]}>
        <a style={{display: "table-cell"}} href={result[3]} target="_blank">
          <h5 className="name-font">{fullname} <span className="score">Score: {result[4]}</span></h5>
        </a>
        <p className="preview-font">{result[2]}</p>
      </div>
      
      )
        
      resultsComponent.push(resultComponent)
    }

     // render the time taken if applicable (after search)
    if (timeTaken !== -1) {
      timeComponent = (
      <div className="time-taken-container">
        <p className='time-taken'>Time taken for query: {timeTaken}s</p>
      </div>
      )  
    }

    // render the pagination numbers
    totalPages = Math.ceil(results.length/RESULTS_PER_PAGE);
    for (let i = 0; i < totalPages; i++) {
      let tmp = (
        <span className="page-numbers" onClick={() => setPageNum(i+1)}>{i+1}</span>
      )
      pagesArr.push(tmp);
    }
  }

  // render the component to show the current page number of results
  let currentPageComponent = null;
  if (totalPages !== 0) {
    currentPageComponent = (
      <div className = "pagination-container">
          <span className="current-page"> 
            Page {pageNum} out of {totalPages}
          </span>
      </div>
    )
  }
  
  return (
    <div>
    <div className="App">
      <header >
        <div className="headerBackground">
          <img src={logo} className="logoImage"></img>
        </div>
      </header>

      {/* Form for taking the query from the user */}
      <div className="form-container">
         
        <Form inline onSubmit={handleSearch} >

              <Form.Control
                placeholder="What would you like to search for?"
                type="text"
                style={{width:"500px", height: "30px"}}
                value = {query}
                onChange = {e => setQuery(e.target.value)}
              />
              <div>
              <Button
                  className="form-button"
                  variant="success"
                  // onClick={handleSearch}
                  type="submit"
              >
                <span hidden={hideSearchSpinner}>
                  <Spinner
                    as="span"
                    animation="border"
                    size="sm"
                    role="status"
                    aria-hidden="true"
                  />
                  <p>Searching</p>Loading...
                </span>
                <span hidden={!hideSearchSpinner}>
                  Search
                </span>
              </Button>

              </div>
        </Form>
      </div>

      {/* TimeTaken component */}
      <div className="time-component">
        {timeComponent}
      </div>

      <div>
        {resultsComponent}
      </div>

    {/* Pagination */}
      {currentPageComponent}
      <div className="pagination-container">
        <div className="pagination">
          
          {pagesArr}
        </div>
      </div>

    </div>
   </div>
  );
}

export default App;