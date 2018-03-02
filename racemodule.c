#include <Python.h>

#include "Lyra2RE.h"

static PyObject *race_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
#if PY_MAJOR_VERSION >= 3
    PyBytesObject *input;
#else
    PyStringObject *input;
#endif
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

#if PY_MAJOR_VERSION >= 3
    lyra2re2_hash((char *)PyBytes_AsString((PyObject*) input), output);
#else
    lyra2re2_hash((char *)PyString_AsString((PyObject*) input), output);
#endif
    Py_DECREF(input);
#if PY_MAJOR_VERSION >= 3
    value = Py_BuildValue("y#", output, 32);
#else
    value = Py_BuildValue("s#", output, 32);
#endif
    PyMem_Free(output);
    return value;
}

static PyMethodDef RaceMethods[] = {
    { "getPoWHash", race_getpowhash, METH_VARARGS, "Returns the proof of work hash using race hash" },
    { NULL, NULL, 0, NULL }
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef RaceModule = {
    PyModuleDef_HEAD_INIT,
    "race_hash",
    "...",
    -1,
    RaceMethods
};

PyMODINIT_FUNC PyInit_race_hash(void) {
    return PyModule_Create(&RaceModule);
}

#else

PyMODINIT_FUNC initrace_hash(void) {
    (void) Py_InitModule("race_hash", RaceMethods);
}
#endif
