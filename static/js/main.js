/**
 * Updates the current color, distance and motor status calling teh corresponding methods
 */
function updateStatus() {
  // Update current color based on Open CV
  updateCurrentColorOpenCV()
  
  // Update motor status
  updateMotorStatusAsync()
  
  // Update current color based on OpenCV
  //...
  
  // Update current distance
  //...
  updateDistanceStatusAsync()

  // update color distance
  updateCurrentColorSensor()
}

/**
 * Update the current color based on OpenCV
 */
 async function updateCurrentColorOpenCV() {
  try {
    // Request color from server
    const requestResult = await requestColorFromOpenCV()
    // Get the HTML element where the status is displayed
    const green_open_cv = document.getElementById('green_open_cv')
    green_open_cv.innerHTML = requestResult.data[0]
    const purple_open_cv = document.getElementById('purple_open_cv')
    purple_open_cv.innerHTML = requestResult.data[1]
    const yellow_open_cv = document.getElementById('yellow_open_cv')
    yellow_open_cv.innerHTML = requestResult.data[2]
  } catch (e) {
    console.log('Error getting the color based on OpenCV', e)
    updateStatus('Error getting the color based on OpenCV')
  }
}

/**
 * Function to request the server to update the current color based on OpenCV
 */
 function requestColorFromOpenCV () {
  try {
    // Make request to server
    return axios.get('/get_color_from_opencv')
  } catch (e) {
    console.log('Error getting the status', e)
    updateStatus('Error getting the status')
  }
}


/**
 * Function to request the server to start the motor
 */
 function requestStartMotor () {
  //...
  try {
    // Make request to server
    return axios.get('/start_motor')
  } catch (e) {
    console.log('Error getting the status', e)
    updateStatus('Error getting the status')
  }
}


/**
 * Function to request the server to stop the motor
 */
 function requestStopMotor () {
  //...
  try {
    // Make request to server
    return axios.get('/stop_motor')
  } catch (e) {
    console.log('Error getting the status', e)
    updateStatus('Error getting the status')
  }
}

/**
 * Update the status of the motor
 * @param {String} status 
 */

 async function updateMotorStatusAsync() {
  try {
    // Request color from server
    const requestResult = await updateMotorStatus(status)
    // Get the HTML element where the status is displayed
    const updateMotorStatusJS = document.getElementById('updateMotorStatusJS')
    updateMotorStatusJS.innerHTML = requestResult.data[0]
  } catch (e) {
    console.log('Error getting the color based on OpenCV', e)
    updateStatus('Error getting the color based on OpenCV')
  }
}
 function updateMotorStatus(status) {
  // Get the HTML element where the status is displayed
  // ...
  try {
    // Make request to server
    return axios.get('/motor_status')
  } catch (e) {
    console.log('Error getting the status', e)
    updateStatus('Error getting the status')
  }
}

/**
 * Update the current color based on distance sensor
 */

 async function updateDistanceStatusAsync() {
  try {
    // Request color from server
    const requestResult = await updateDistance()
    // Get the HTML element where the status is displayed
    const updateDistanceStatusJS = document.getElementById('updateDistanceStatusJS')
    updateDistanceStatusJS.innerHTML = requestResult.data
  } catch (e) {
    console.log('Error getting the color based on OpenCV', e)
    updateStatus('Error getting the color based on OpenCV')
  }
}
 function updateDistance() {
  // Get the HTML element where the status is displayed
  // ...
  try {
    // Make request to server
    return axios.get('/update_distance')
  } catch (e) {
    console.log('Error getting the status', e)
    updateStatus('Error getting the status')
  }
}


/**
 * Function to request the server to get the distance from
 * the rod to the ultrasonic sensor
 */
 function requestDistance () {
  //...
  try {
    // Make request to server
    return axios.get('/get_distance')
  } catch (e) {
    console.log('Error getting the status', e)
    updateStatus('Error getting the status')
  }
}


/**
 * Update the current color based on distance sensor
 */
 async function updateCurrentColorSensor() {
  try {
    // Request color from server
    const requestResult = await updateCurrentColorDistance()
    // Get the HTML element where the status is displayed
    const green_sensor = document.getElementById('green_sensor')
    green_sensor.innerHTML = requestResult.data[0]
    const purple_sensor = document.getElementById('purple_sensor')
    purple_sensor.innerHTML = requestResult.data[1]
    const yellow_sensor = document.getElementById('yellow_sensor')
    yellow_sensor.innerHTML = requestResult.data[2]
  } catch (e) {
    console.log('Error getting the color based on OpenCV', e)
    updateStatus('Error getting the color based on OpenCV')
  }
}

 function updateCurrentColorDistance() {
  // Get the HTML element where the status is displayed
  // ...
  try {
    // Make request to server
    return axios.get('/get_color_from_distance')
  } catch (e) {
    console.log('Error getting the status', e)
    updateStatus('Error getting the status')
  }
}

/**
 * Function to request the server to get the color based
 * on distance only
 */
 function requestColorFromDistance () {
  //...
}
