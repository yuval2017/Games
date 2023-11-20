import React from 'react';
import {
  RouterProvider,
  createBrowserRouter,
  createRoutesFromElements,
  Route,
} from 'react-router-dom';
import Chat, {loader as chatLoader} from './Chat';
const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/">
      <Route index element={<h1>Hey</h1>} />
      <Route path="chat/:room" element={<Chat />} loader={chatLoader} /> {/* Use <Chat /> directly */}
    </Route>
  )
);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
