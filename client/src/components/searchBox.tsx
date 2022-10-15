import React, { ReactElement, useState } from "react";
import { Box, TextField, IconButton } from "@mui/material";
import AddIcon from "@mui/icons-material/Add";

const SearchBox = (): ReactElement => {
  const [searchInput, setSearchInput] = useState("");

  const searchItem = async () => {
    const response = await fetch("http://127.0.0.1:5000/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
    });
    const data = await response.json();
    console.log(data);
  };

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
        multiline
      />
    </Box>
  );
};

export default SearchBox;