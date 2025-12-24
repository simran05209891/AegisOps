import React, { useEffect, useState } from "react";
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend
} from "recharts";

function App() {
  const [data, setData] = useState([]);
  const [status, setStatus] = useState("NORMAL");

  useEffect(() => {
    const interval = setInterval(() => {
      const temp = Math.floor(Math.random() * 100);
      const cpu = Math.floor(Math.random() * 100);
      const mem = Math.floor(Math.random() * 100);

      const alert = (temp > 80 || cpu > 85 || mem > 85)
        ? "ALERT"
        : "NORMAL";

      setStatus(alert);
      setData(prev => [
        ...prev.slice(-9),
        {
          time: new Date().toLocaleTimeString(),
          temperature: temp,
          cpu: cpu,
          memory: mem
        }
      ]);
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>
      <h1>🚀 AegisOps</h1>
      <h3>DevOps-Driven IoT Infrastructure Monitoring Platform</h3>
      <p><b>Developed by:</b> Simran Anand</p>

      <h2>
        System Status:
        {status === "ALERT" ? " 🔴 ALERT" : " 🟢 NORMAL"}
      </h2>

      <LineChart width={850} height={400} data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="time" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="temperature" stroke="#ff7300" />
        <Line type="monotone" dataKey="cpu" stroke="#387908" />
        <Line type="monotone" dataKey="memory" stroke="#8884d8" />
      </LineChart>
    </div>
  );
}

export default App;
