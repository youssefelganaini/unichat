import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark align-center">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">Manifesto.ai</a>
        </div>3
      </nav>
      <div className="container bg-dark d-flex align-items-center justify-content-center" style={{ minHeight: '100vh' }}>
        <div>

          <h1 className="text-white">Manifesto.ai</h1>
          <div className="container container-half">
            <p className="lead text-white mx-auto paragraph-width">
              I believe that staying up to date with news nowadays is a huge pain.
              So I built a tool that gives me what I need to know and leaves me with ideas to reflect on.
            </p>
          </div>
        </div>
      </div>
    </>

  )
}

export default App
