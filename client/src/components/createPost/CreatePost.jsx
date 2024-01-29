import React from 'react'
import Header from '../header/Header'
import CreatePostForm from './CreatePostForm'


const CreatePost = () => {
  return (
    <div className='create-post'>
        <Header/>
        <CreatePostForm/>
    </div>
  )
}

export default CreatePost