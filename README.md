# AngularFlaskExample

This is an example of how to host an angular app with simple python backend (flask) so it is easy to add backend apis on the same port that is hosting the site.

This was created by using ng cli to generate the project, and then adding the server/ directory with a flask app that hosts the project.

In order to run the whole project locally, run

```
ng build && npm start
```
This will build the angular project and start the flask app.

To just run the angular project with automatic refresh you can still use `ng serve`.

This project can also be deployed to Heroku as-is. The npm script `heroku-postbuild` automatically builds the angular project before heroku tries to launch the flask app.

When adding new npm dependencies, make sure they are added as `dependencies` instead of `devDependencies` if they are needed to run `ng build`



This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 11.2.11.