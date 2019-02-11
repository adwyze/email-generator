# Emails Generator

### What and why?

This repository contains the generator for HTML templates. The generator uses Inky(by Foundation) for templating language that converts simple HTML tags into the complex table HTML required for emails.

A few basic components(Buttons, Greetings, etc) required are already written in the [index.html](./src/pages/index.html)

For creating a new template, say `Invitation.html`, just add a HTML page at `./src/pages/` and on running the build, the template will be generated at `./dist/`

### Setup

```
    yarn install
    yarn start
```

For generating the production-ready templates, run

```
    yarn build
```

### Writing HTML templates just got easy, now what?

The generated templates can be hosted on Mailchimp(/Mandrill) or some other service. Mandrill in particular provides a REST API for targeting a hosted template and injecting the content/variables into the same. And sending the mail right away. 🎉

### References

- [Foundation - Inky](https://foundation.zurb.com/emails/docs/inky.html)
- [Manrill](http://mandrillapp.com/api/docs/templates.ruby.html)
