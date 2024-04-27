import React from 'react'
import Category from './adminComponents/Category'

const page = () => {
    return (
        <main className='w-full bg-gradient-to-r from-black via-slate-900 to-blue-950 h-screen'>
            <h1 className='flex justify-center items-center font-serif font-bold md:text-4xl text-3xl text-white  h-20'>
                Admin Dashboard
            </h1>
            <section>
                <Category />
            </section>
        </main>
    )
}

export default page