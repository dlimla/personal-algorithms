function truckTour(petrolpumps) {
    // two pointers - a pointer starting at 0
    // start and current pointer at 0
    // currentGas starts at 0
    let startPointer = 0;
    let currPointer = 0;
    let currGas = 0;
    
    // while loop until start === current
    while (startPointer < petrolpumps.length) {
      // [petrol, distance]
      // fill up, and check distance
      // add the petrol to our currentGas
      currGas += petrolpumps[currPointer][0];
      // subtract the distance from our gas
      currGas -= petrolpumps[currPointer][1];
      // if our current gas is > 0, then we've made it to the next station
      if (currGas >= 0) {
        // move our current pointer to the next station
        
        currPointer++;
        if (currPointer === petrolpumps.length) {
          currPointer = 0;
        }
        // check if current === start, then we return start
        if (currPointer === startPointer) {
          return currPointer
        }
      } else {
        // if we can't make it
        // reset currentGas
        // move start and current to the next station
        currGas = 0;
        startPointer++;
        currPointer = startPointer;
      }
    }
      
  }