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
