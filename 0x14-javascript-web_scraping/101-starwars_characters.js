#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;
    const characters = [];

    function fetchCharacter (index) {
      if (index >= characterUrls.length) {
        characters.forEach((characterName) => {
          console.log(characterName);
        });
        return;
      }

      const characterUrl = characterUrls[index];
      request(characterUrl, (characterError, characterResponse, characterBody) => {
        if (characterError) {
          console.error(characterError);
        } else if (characterResponse.statusCode === 200) {
          const characterData = JSON.parse(characterBody);
          characters.push(characterData.name);
          fetchCharacter(index + 1);
        } else {
          console.error(`Request failed with status code: ${characterResponse.statusCode}`);
        }
      });
    }

    fetchCharacter(0);
  } else {
    console.error(`Request failed with status code: ${response.statusCode}`);
  }
});
