import React from 'react';

//Komponenta koja omogućava korisnicima da pretražuju terene, termine, timove, ostale korisnike itd.

function Search() {
  return (
    <div>
      <h1>Search Page</h1>
      <form>
        <div>
          <label>Search:</label>
          <input type="text" name="search" />
        </div>
        <button type="submit">Search</button>
      </form>
    </div>
  );
}

export default Search;
