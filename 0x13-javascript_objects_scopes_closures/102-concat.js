#!/usr/bin/node

// Get the file paths from the arguments
var file1Path = process.argv[2];
var file2Path = process.argv[3];
var destPath = process.argv[4];

// Read the source files
var file1 = fs.readFileSync(file1Path, 'utf8');
var file2 = fs.readFileSync(file2Path, 'utf8');

// Concat the source files
var result = file1 + file2;

// Write the concatenated file to the destination
fs.writeFileSync(destPath, result);
