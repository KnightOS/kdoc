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

And then run `python -m kdoc file1.asm file2.asm ...` to get docs in html/.
