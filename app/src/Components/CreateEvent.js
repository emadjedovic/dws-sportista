import React from 'react';

// Ova komponenta omogućava korisnicima da kreiraju termine (i ostalo?).

function CreateEvent() {
  return (
    <div>
      <h1>Create Event Page</h1>
      <form>
        <div>
          <label>Event Name:</label>
          <input type="text" name="eventName" />
        </div>
        <div>
          <label>Date:</label>
          <input type="date" name="date" />
        </div>
        <div>
          <label>Location:</label>
          <input type="text" name="location" />
        </div>
        <button type="submit">Create Event</button>
      </form>
    </div>
  );
}

export default CreateEvent;
