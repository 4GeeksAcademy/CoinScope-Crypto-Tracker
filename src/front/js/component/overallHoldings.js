import React, { useState, useEffect, useContext } from "react";
import PropTypes from "prop-types";
import { Link, useParams, useNavigate } from "react-router-dom";
import { Context } from "../store/appContext";

export const OverallHoldings = () => {
    const { store, actions } = useContext(Context);
    const timestamp = Date.now()

    // useEffect (()=>{
    //     store.walletReturnsData.map((coin)=> )
    // },[])

    return (
        <div>overallholdings</div>
    )

}