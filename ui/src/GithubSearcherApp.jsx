
import { Searcher } from "./components/Searcher/Searcher";
import "./index.css";
import { useEffect, useState } from "react";
import axios from 'axios';
import { User } from "./components/Widget/User";
import { Repository } from "./components/Widget/Repository";
import { Issue } from "./components/Widget/Issue";

export const GithubSearcherApp = () => {

    const [showResults, setShowResults] = useState(false);
    const [results, setResults] = useState([])
    const [entitySelected, setEntitySelected] = useState('users')
    //const [entitySelected, setEntitySelected] = useState('users')
    //const [searchCriteria, setSearchCriteria] = useState('')

    useEffect(() => {
        if(showResults == true){
            document.getElementById('root').style.setProperty('--top', '0%');
            document.getElementById('root').style.setProperty('--transform', '');
        }else{
            document.getElementById('root').style.setProperty('--top', '46%');
        }
        
    }, [showResults]);
    return (
        <>
            <Searcher entitySelected={entitySelected} setShowResults={setShowResults} setResults={setResults} setEntitySelected={setEntitySelected} />
            <section key="results" id="results">
                {
                    showResults &&
                    results.map(d => {
                        if (entitySelected === 'users') {
                            return <User data={d}></User> 
                        }

                        if (entitySelected === 'repositories') {
                            return <Repository data={d}></Repository>
                        }

                        return <Issue data={d}></Issue>

                    })
                }
                
            </section>
        </>
    );
}