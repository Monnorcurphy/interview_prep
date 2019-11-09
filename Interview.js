//Implement an algorithm to determine if a string has all unique characters. 

const isUnique = (string) => {
    const dictionary = {};
    let unique = true;
    string.split('').forEach(char =>{
        if(dictionary.hasOwnProperty(char)){
            unique = false;
        }else{
            dictionary[char] = true;
        }
    })

    return unique
}

//What if you cannot use additional data structures?

const isUniqueTwo = (string) => {
    let unique = true;
    for (first in string){
        for(second in string){
            if(first !== second && string[first] === string[second]){
                unique = false;
            }
        }
    }
    return unique
}

//Given two strings, write a method to decide if one is a permutation of the other

const permutation = (first, second) => {
    if(first.length !== second.length){
        return false
    }
    
    let dict = {};
    let permutation = true;
    for (idx in first){
        if(dict.hasOwnProperty(first[idx])){
            dict[first[idx]] += 1;
        }else{
            dict[first[idx]] = 1;
        }
    }

    for (idx in second){
        if(dict.hasOwnProperty(second[idx])){
            dict[second[idx]] -= 1;
            if (dict[second[idx]] <= -1){
                permutation = false;
            }
        }else{
            permutation = false;
        }
    }
    return permutation
}


// write a method to replace all the spaces in a string with %20

const urlify = (string) => {
    return string.replace(' ', '%20')
}