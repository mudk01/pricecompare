import React, { ReactElement, useState, useEffect } from "react";
import { Box, TextField, IconButton } from "@mui/material";
import AddIcon from "@mui/icons-material/Add";

const styles = {
  compareBox: {
    display: "flex",
    flexDirection: "row",
    justifyContent: "space-evenly",
    alignItems: "center" as const,
  },
};

const SearchBox = (): ReactElement => {
  const [searchInput, setSearchInput] = useState("");
  const [items, setItems] = useState([{}]);

  const searchItem = async () => {
    const url = `http://127.0.0.1:5000/compare/${searchInput}`;
    const response = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();
    console.log(data);
    setItems(data);
    console.log(items);
    console.log(data[0]);
  };

  useEffect(() => {}, []);

  const handleSearchInput = (event: {
    target: { value: React.SetStateAction<string> };
  }): void => {
    setSearchInput(event.target.value);
  };

  const handleEnterKey = (event: { key: string }): void => {
    if (event.key === "Enter") {
      searchItem();
    }
  };

  return (
    <Box>
      <TextField
        fullWidth
        InputLabelProps={{ shrink: false }}
        InputProps={{
          endAdornment: (
            <IconButton onClick={searchItem}>
              <AddIcon />
            </IconButton>
          ),
        }}
        onKeyPress={handleEnterKey}
        placeholder="Search for an item"
        onChange={handleSearchInput}
        value={searchInput}
      />
      <Box sx={styles.compareBox}>
        <Box>
          <h1>Target</h1>
          {/* {items[0].map((key, value) => {
            return <li>{item}</li>;
          })} */}
        </Box>
        <Box>
          <h1>Walmart</h1>
        </Box>
      </Box>
    </Box>
  );
};

export default SearchBox;
