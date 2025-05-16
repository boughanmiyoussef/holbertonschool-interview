#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  printCharacters(characters, 0);
});

function printCharacters (charList, index) {
  if (index >= charList.length) return;

  request(charList[index], (error, response, body) => {
    if (!error) {
      const character = JSON.parse(body);
      console.log(character.name);
      printCharacters(charList, index + 1);
    }
  });
}
