import React, { ReactElement } from "react";
import scrapeSite from "./webScraping/test";

const App = (): ReactElement => {
  return (
    <div>
      <body>
        <h1>HELLO</h1>
        <button
          onClick={() =>
            scrapeSite().then((result: string) => console.log(result))
          }
        >
          Press me to run python
        </button>
      </body>
    </div>
  );
};

export default App;
