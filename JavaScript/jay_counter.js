var rl = require('readline-sync');
if (rl.keyInYN(['uWu whats dis would you wike to stwart couwnting? :3']) === true) {
    var input = rl.questionInt(['pwease enter any whole numbwer oWo :']);
    var fancyUi = require('readline-sync'), value = 0;
    console.log('[type uwu and press enter to proceed, my demands are clear.]\n');
    while (value <= input) {
        console.log('\x1B[1A\x1B[K|' +
            (new Array(value + 1)).join('-') + 'O' +
            (new Array(input - value + 1)).join('-') + '| ' + value);
        var uwu = fancyUi.prompt('', {
            hideEchoBack: true, mask: ''
        });
        if (uwu === 'uwu') {
            if (value < input) {
                value++;
            }
            else {
                break;
            }
        }
    }
}
else {
    console.log('if you can\'t count me at my uWu you don\'t deserve to count me at my oWo');
}
