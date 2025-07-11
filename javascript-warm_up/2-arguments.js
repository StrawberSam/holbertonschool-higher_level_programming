#!/usr/bin/node

// Récupère uniquement les arguments passés au script
// (sans 'node' et le chemin du script)
const args = process.argv.slice(2);

if (args.length === 0) {
  console.log("No argument");
} else if (args.length === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
