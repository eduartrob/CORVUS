import { initializeApp } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-app.js";
import { getAuth, GoogleAuthProvider, signInWithPopup, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-auth.js";
import { getFirestore, collection, addDoc, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyD7y9TOb6SzLFQoQKnWzBr-G3-O_8AaNvM",
  authDomain: "corvus-376d3.firebaseapp.com",
  projectId: "corvus-376d3",
  storageBucket: "corvus-376d3.firebasestorage.app",
  messagingSenderId: "1078483343139",
  appId: "1:1078483343139:web:eacec0370df0c562b4de96",
  measurementId: "G-MFC7DEXC28"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);
const googleProvider = new GoogleAuthProvider();

export { auth, db, googleProvider, signInWithPopup, signInWithEmailAndPassword, collection, addDoc, serverTimestamp };
