// append some text to a pre element.
function prependOut(text) {
    var mypre = document.getElementById("clrs-output");
    mypre.innerHTML = mypre.innerHTML + text;
}
function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
        throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

// Grab the code, get a reference to output
// configure the output function and call Sk.importMainWithBody()
function runit() {
    var prog = document.getElementById("clrs-code").value;
    var mypre = document.getElementById("clrs-output");
    mypre.innerHTML = '';
    Sk.pre = "output";
    Sk.configure({output:prependOut, read:builtinRead});
    var myPromise = Sk.misceval.asyncToPromise(function() {
        return Sk.importMainWithBody("<stdin>", false, prog, true);
    });
    myPromise.then(
        function(mod) {
            mypre.style.color = "#333";
            console.log('success');
        },
        function(err) {
            mypre.style.color = "#f00";
            mypre.innerHTML = err.toString();
            console.log(err.toString());
    });
}