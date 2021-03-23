# Emails Generator

### What and why?

This repository contains the generator for HTML templates. The generator uses Inky(by Foundation) as templating language that converts simple HTML tags into the complex table HTML required for emails.

A few basic components(Buttons, Greetings, etc) required are already written in the [index.html](./src/pages/index.html)

For creating a new template, say `Invitation.html`, just add a HTML page named `Invitation.html` at `./src/pages/` and on running the build, the template will be generated at `./dist/Invitation.html`

### Setup
The setup needs `gulp` to be globally installed.

```
    yarn install
    yarn start
```

The setup uses `browser-sync`, making it easy to test the templates on different devices connected to the same network.

For generating the production-ready templates, run

```
    gulp build
```

### Writing HTML templates just got easy, now what?

The generated templates can be hosted on Mailchimp(/Mandrill) or some other service. Mandrill in particular provides a REST API for targeting a hosted template and injecting the content/variables into the same. And send the mail right away. 🎉

### References

- [Foundation - Inky](https://foundation.zurb.com/emails/docs/inky.html)
- [Mandrill](http://mandrillapp.com/api/docs/templates.ruby.html)

## Publish updated template to Mailchimp

#### install pipenv
- run `pip install pipenv`


#### install dependencies
- run `cd email-generator`
- run `pipenv sync`


#### activate the virtual environment
- run `pipenv shell`


#### publish the new built templates
- run `python mandrill_operations.py --key your-mandrill-key --operation update --email acb.xyz@fff.com --template_name anomaly-alert --file_name anomalyAlert.html`
