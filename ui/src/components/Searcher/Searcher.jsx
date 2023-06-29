import PropTypes from 'prop-types';
import "./searcher.css";
import { useEffect, useMemo, useState } from "react";
import axios from 'axios';
import { debounce } from 'lodash';

export const Searcher = ({entitySelected, setShowResults, setResults, setEntitySelected}) => {
    
    const [searchCriteria, setSearchCriteria] = useState('')
    const handleChange = (event) => {
        const inputValue = event.target.value
        setSearchCriteria(inputValue)
        if (inputValue.length >= 3) {
            setShowResults(true)
        } else {
            setShowResults(false)
        }
    }

    const debouncedChangeHandler = useMemo(
         () => debounce(handleChange, 500)
    , [])

    useEffect(() => {
       if (searchCriteria.length >= 3 && entitySelected.length > 0) { 
        const payload = {
            search_criteria: searchCriteria,
            entity_type: entitySelected
        }
        axios.post(`/api/search`, payload)
    .then((response) => {
        const result = response.data
        setResults([...result])
    })
    .catch((error) => {
        console.error(`Error: ${error}`);
    });
       } 
    }, [searchCriteria, entitySelected]);


    

    const handleChangeEntitySelected = (event) => {
        setEntitySelected(event.target.value)
    }

    return (
        <>
            <header id="header-content">
                <i className="fa-brands fa-github fa-2xl"></i>
                <div id="title">
                    <p>GitHub Searcher</p>
                    <span>Search users or repositories below</span>
                </div>
            </header>
            <section id="search">
                <input 
                    type="text" 
                    placeholder="Start typing to search .."
                    onChange={debouncedChangeHandler}
                />
                <select onChange={handleChangeEntitySelected} name="entities" id="entities">
                    <option value="users">Users</option>
                    <option value="repositories">Repository</option>
                    <option value="issues">Issue</option>
                </select>
            </section>
        </>
    );
}
Searcher.propTypes = {
    setShowResults: PropTypes.func
}