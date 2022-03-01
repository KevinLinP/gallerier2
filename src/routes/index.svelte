<script>
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "firebase/app";

  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  const firebaseConfig = {
    apiKey: import.meta.env.VITE_apiKey,
    authDomain: `${import.meta.env.VITE_projectId}.firebaseapp.com`,
    projectId: import.meta.env.VITE_projectId,
    appId: import.meta.env.VITE_appId
  };


  console.log(firebaseConfig)

  let user

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);

  // auth
  import { getAuth, signInWithPopup, GoogleAuthProvider, onAuthStateChanged } from "firebase/auth";
  const provider = new GoogleAuthProvider();
  const auth = getAuth();

  console.log(auth)

  onAuthStateChanged(auth, (authUser) => {
    user = authUser

    if (user) {
      console.log('user', user)
      logImages()
    }
  });

  function loginClicked() {
    signInWithPopup(auth, provider)
      .then((result) => {
        // This gives you a Google Access Token. You can use it to access the Google API.
        const credential = GoogleAuthProvider.credentialFromResult(result);
        const token = credential.accessToken;
        // The signed-in user info.
        const user = result.user;
        // ...
      }).catch((error) => {
        // Handle Errors here.
        const errorCode = error.code;
        const errorMessage = error.message;
        // The email of the user's account used.
        const email = error.email;
        // The AuthCredential type that was used.
        const credential = GoogleAuthProvider.credentialFromError(error);
        // ...
      });
  }

  function logoutClicked() {
    auth.signOut()
  }

  import { getFirestore, collection, query, where, getDocs } from "firebase/firestore";

  const db = getFirestore()

  async function logImages() {
    const q = query(collection(db, "images"));

    const querySnapshot = await getDocs(q);
    const images = []
    querySnapshot.forEach((imageSnapshot) => {
      images.push(imageSnapshot.data())
    });
    console.log('images', images)
  }
</script>

{#if user}
  logged in
  <button on:click={logoutClicked}>log out</button>
{:else if user === null}
  <button on:click={loginClicked}>log in with Google</button>
{/if}