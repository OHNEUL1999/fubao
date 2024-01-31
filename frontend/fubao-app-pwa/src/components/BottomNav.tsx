import React, { Fragment, useState } from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";

const NavBar = styled.nav`
  display: flex;
  width: 100vw;
  max-width: 576px;
  margin: auto;
  justify-content: space-evenly;
  background-color: #ffffff;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 0.2em 0em;
  box-shadow: 1px 1px 5px 1px #d1d1d1;
`;

const NavItem = styled.div`
  /* border: 1px solid black; */
  width: 20vw;
  text-align: center;
  padding: 1vh;
  cursor: pointer;
`;

const NavCenterItem = styled.div`
  position: fixed;
  border: 3px solid #168bf2;
  border-radius: 50%;
  width: 3rem;
  height: 3rem;
  bottom: 0;
  left: 50%;
  transform: translate(-50%, 0);
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: white;
  cursor: pointer;
  margin-bottom: 0.1rem;
`;

const BottomNav = () => {
  return (
    <Fragment>
      <NavBar>
        <Link to="/viewall" style={{ textDecoration: "none" }}>
          <NavItem>전체보기</NavItem>
        </Link>
        <NavItem>d</NavItem>
        <Link to="/map" style={{ textDecoration: "none" }}>
          <NavItem>지도</NavItem>
        </Link>
      </NavBar>
      <Link to="/collection">
        <NavCenterItem>
          <img
            src="/imgs/collection_font.png"
            alt="to_collection"
            style={{ width: "3rem", height: "1.8rem" }}
          />
        </NavCenterItem>
      </Link>
    </Fragment>
  );
};

export default BottomNav;
