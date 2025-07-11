#!/usr/bin/node

const args = process.argv.slice(2); // récupère les arguments passés au script (hors node et fichier)

if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
