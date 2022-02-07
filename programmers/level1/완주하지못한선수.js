#answer1
function solution(participant, completion) {
    const obj = {}

    for (let p of participant) {
        obj[p] = obj[p] ? obj[p] + 1 : 1;
    }
    for (let c of completion) {
        obj[c] -= 1;
    }
    for (let key in obj) {
        if (obj[key] == 1) {
            return key;
        }
    }
}

#answer2
function solution(participant, completion) {
    const n = participant.length;
    let answer = '';

    participant.sort();
    completion.sort();

    for (let i = 0; i < n; i++){
        if (participant[i] !== completion[i]) {
            answer = participant[i];
            return answer;
        }
    }
}