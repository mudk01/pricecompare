import { loadPyodide } from "pyodide"

const scrapeSite = async () => {
    const pyodide = await loadPyodide();
    const script = `
        print('hello')
    `;
    // const pyodide = window.pyodide;

    return pyodide.runPythonAsync(script);
}

export default scrapeSite;