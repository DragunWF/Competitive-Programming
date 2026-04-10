// https://www.codewars.com/kata/5262fa26875ed24a3e000029

function roomMates(rooms, floor) {
  return rooms.filter((client, index) => {
    const currentFloor = Math.ceil((index + 1) / 6);
    return currentFloor === floor && client;
  });
}

function roomMatesWithoutFilter(rooms, floor) {
  const clients = [];
  for (let i = 0, roomNo = 1; i < rooms.length; i++, roomNo++) {
    const currentFloor = Math.ceil(roomNo / 6);
    if (currentFloor === floor && rooms[i]) {
      clients.push(rooms[i]);
    } else if (currentFloor > floor) {
      break;
    }
  }
  return clients;
}
