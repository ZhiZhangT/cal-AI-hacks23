import React, { useRef, useState } from 'react';
import Webcam from 'react-webcam';

function VideoPlayer() {
  const webcamRef = useRef(null);
  const [recording, setRecording] = useState(false);

  const handlePlay = () => {
    webcamRef.current.startRecording();
    setRecording(true);
  };

  const handlePause = () => {
    webcamRef.current.stopRecording();
    setRecording(false);
    const videoBlob = webcamRef.current.getRecording();
    console.log(videoBlob);
    // Can send the videoBlob to your backend for further processing
  };

  console.log(webcamRef);

  return (
    <div>
      <Webcam audio={false} ref={webcamRef} />
      <video src="../../backend/videos/Distributed Systems - Fast Tech Skills.mp4" onPlay={handlePlay} onPause={handlePause} controls />
    </div>
  );
}

export default VideoPlayer;