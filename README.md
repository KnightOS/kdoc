# kdoc

This tool generates documentation for assembly projects. Write your code like this:

    ;; functionName [Category]
    ;;  Description description description description
    ;;  description description description description
    ;;  description description description
    ;; Inputs:
    ;;  Register: description
    ;;  Register: description
    ;; Outputs:
    ;;  Register: description

And then run `python -m kdoc categories.yaml $(cd kernel && git log -1 --format=%H) $(find kernel/src -type f)` to get docs in html/.

## Help, Bugs, Feedback

If you need help with KnightOS, want to keep up with progress, chat with
developers, or ask any other questions about KnightOS, you can hang out in the
IRC channel: [#knightos on irc.freenode.net](http://webchat.freenode.net/?channels=knightos).
 
To report bugs, please create [a GitHub issue](https://github.com/KnightOS/KnightOS/issues/new) or contact us on IRC.
 
If you'd like to contribute to the project, please see the [contribution guidelines](http://www.knightos.org/contributing).
