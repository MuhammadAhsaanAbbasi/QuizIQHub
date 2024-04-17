"use client"

import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import Button from '@/components/layout/Button';
import { FormType } from '@/lib/utils/types';
import Link from 'next/link';
import { setCookie } from 'cookies-next';

const page = () => {

  let formData = new FormData();
  const [error, setError] = useState();
  const { register, handleSubmit } = useForm<FormType>();

  const loginFn = async (data: FormType) => {

    formData.append("username", "bilal");
    // formData.append("password", data.user_password)

    const response = await fetch(`http://localhost:8000/api/Signin`,
      {
        method: "POST",
        headers: {
          "content-type": "application/json"
        },
        body: JSON.stringify(data)
      }
    );
    if (!response.ok) {
      setError(await response.json())
    }else{
      const tokens_data = await response.json()
      
      // TODO: set tokens in cookies
      // setCookie()

      // console.log(formData.values);
      console.log(formData);
    }
  };
  return (
    <main className='h-screen flex justify-center items-center bg-gradient-to-tr from-black via-slate-950 to-blue-950'>

      <div className='w-1/3 p-6 rounded-md bg-slate-600 flex flex-col gap-2 justify-center items-center'>
        <h1 className='md:text-2xl text-xl font-bold text-gray-900 m-2'>Welcome to Quiz Hub</h1>
        <p className='text-red-500'>{error ? error : ""}</p>
        <form onSubmit={handleSubmit(loginFn)} className='flex flex-col gap-4 justify-center items-center'>
          {/* 
          <input className='rounded-md border  p-1.5' type="text" placeholder='userName'  {...register("user_name", {
            required: true,
            // pattern:"^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$"
          })} /> */}

          <input className='rounded-md border p-1.5' type="email" placeholder='userEmail' {...register("user_email", {
            required: true
          })} />
          <input className='rounded-md border p-1.5' type="password" placeholder='userPassword' {...register("user_password", {
            required: true,
            minLength: 6
          })} />
          <Button buttonType='submit'>
            Sign In
          </Button>
        </form>

        <h1 className='md:text-xl text-gray-900 m-2'>
          Don't have an account?
        </h1>
        <Link href={"/register"}>
          <Button buttonType='button'>
            Sign Up
          </Button>
        </Link>
      </div>
    </main>
  )
}

export default page


//  How register works?

// {
//   user_name:"bilal"
// }
// {
//   user_name:"bilal",
//   user_email: "bilal2gmil.vom"
// }
// {
//   user_name:"bilal",
//   user_email: "bilal2gmil.vom",
//   user_password:"bilal123"
// }