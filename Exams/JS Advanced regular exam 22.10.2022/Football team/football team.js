class footballTeam {
    constructor(clubName, country) {
        this.clubName = clubName;
        this.country = country;
        this.invitedPlayers = [];
    };

    newAdditions(footballPlayers) {
        footballPlayers.forEach(player => {
            let [name, age, playerValue] = player.split('/');
            age = Number(age);
            playerValue = Number(playerValue);
        let currentPlayer = this.invitedPlayers.find(pl => pl.name === name);

        if (!currentPlayer) {
            this.invitedPlayers.push({
                name,
                age,
                playerValue
            });
        } else {
            if (currentPlayer.playerValue > playerValue) {
                this.invitedPlayers.playerValue = currentPlayer.playerValue;
                };
            };
        });
        let result = [];
        this.invitedPlayers.forEach(player => result.push(player.name));
        return `You successfully invite ${result.join(', ')}.`;
    };

    signContract(selectedPlayer) {
        let [name, playerOffer] = selectedPlayer.split('/');
        playerOffer = Number(playerOffer);
        let currentPlayer = this.invitedPlayers.find(pl => pl.name === name);

        if (!currentPlayer) {
            throw new Error(`${name} is not invited to the selection list!`);
        };
        if (playerOffer < currentPlayer.playerValue) {
            let priceDifference = currentPlayer.playerValue - playerOffer;
            throw new Error(`The manager's offer is not enough to sign a contract with ${name}, ${priceDifference} million more are needed to sign the contract!`);
        };
        currentPlayer.playerValue = "Bought";
        return `Congratulations! You sign a contract with ${currentPlayer.name} for ${playerOffer} million dollars.`
        };

    ageLimit(name, age) {
        age = Number(age);
        let currentPlayer = this.invitedPlayers.find(pl => pl.name === name);
        if (!currentPlayer) {
            throw new Error(`${name} is not invited to the selection list!`);
        };
        if (currentPlayer.age < age) {
            let ageDifference = age - currentPlayer.age;
            if (ageDifference < 5) {
                return `${name} will sign a contract for ${ageDifference} years with ${this.clubName} in ${this.country}!`;
            } else {
                return `${name} will sign a full 5 years contract for ${this.clubName} in ${this.country}!`;
            };
        } else {
            return `${name} is above age limit!`;
        };
    };

    transferWindowResult() {
        let result = "Players list:\n";
        this.invitedPlayers.sort((a, b) => b - a).forEach(pl => result += `Player ${pl.name}-${pl.playerValue}\n`);
        result = result.substring(0, result.length - 1);
        return result;
    };    
}
