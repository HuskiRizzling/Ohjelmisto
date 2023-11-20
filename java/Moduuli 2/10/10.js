`use strict`;
const numbercand = prompt(`How many candidates are there?`);
const names = [];
for (let i = 1; i <= numbercand; i++) {
      const namecand = prompt(`Enter the name of the candidate ` + i + `:`);
      names.push({name: namecand, votes: 0});
}

const numbervoters = prompt(`How many voters are there?`);
for (let i = 1; i <= numbervoters; i++) {
      const vote = prompt(`Who would you like to vote for voter ` + i + `? Write the name or leave empty for an empty vote.`);
      const pickcand = names.find(candidate => candidate.name === vote)
      if (pickcand) pickcand.votes++;
}
names.sort((i, j) => j.votes - i.votes)
console.log(`The winner is ${names[0].name} with ${names[0].votes} votes.`);
console.log(`Results:`);
for (let i = 0; i <= numbercand; i++) {
  console.log(`${names[i].name}: ${names[i].votes} votes`);
}