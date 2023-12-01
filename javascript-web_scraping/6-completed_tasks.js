#!/usr/bin/node
// computes the number of tasks completed by user id.
const req = require('request');
const url = process.argv[2];

req(url, (e, response, data) => {
  if (e) {
    process.exit(1);
  }
  const todos = JSON.parse(data);
  const finishedTodos = {};
  todos.forEach((todo) => {
    if (todo.completed) {
      if (finishedTodos[todo.userId]) {
        finishedTodos[todo.userId]++;
      } else {
        finishedTodos[todo.userId] = 1;
      }
    }
  });
  console.log(finishedTodos);
});
