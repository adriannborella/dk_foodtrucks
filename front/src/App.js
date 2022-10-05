import "./App.css";
import { Navigation } from "./routes";
import { ToastContainer } from "react-toastify";

function App() {
  
  return (
    <div className="App">
      <Navigation></Navigation>
      <ToastContainer
        position="bottom-center"
        autoClose={5000}
        hideProgressBar
        newestOnTop
        closeOnClick
        rtl={false}
        draggable
        pauseOnHover={false}
      />
    </div>
  );
}

export default App;
