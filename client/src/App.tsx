import React, { ReactElement } from "react";
import SearchBox from "./components/searchBox";

const styles = {
  divStyle: {
    textAlign: "center" as const,
  },
};

const App = (): ReactElement => {
  return (
    <div>
      <h1 style={styles.divStyle}>Welcome to Price Comparer</h1>
      <SearchBox />
    </div>
  );
};

export default App;
