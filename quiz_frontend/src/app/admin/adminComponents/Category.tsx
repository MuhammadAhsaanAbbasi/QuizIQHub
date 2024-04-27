"use client"
import Button from '@/components/layout/Button'
import React, { useState } from 'react'
import { useForm } from 'react-hook-form'
import { CategoryType } from '@/lib/utils/types'

const Category = () => {
    const { register, handleSubmit } = useForm<CategoryType>();
    const [error, setError] = useState("");
    const set_category = async (data: CategoryType) => {
        const response = await fetch("/api/add_category", {
            method: "POST",
            headers: {
                "content-type": "application/json"
            },
            body: JSON.stringify(data)
        });
        const res_data = await response.json();
        if (!response.ok) {
            setError(res_data);    
        }else{
            setError("");
            console.log(res_data);
        }
        
        // console.log(await response.json());
    };
    return (
        <main className='shadow-[inset_17px_-28px_23px_0px_#0C1221] rounded-md m-4 p-5 flex flex-col gap-3 w-full bg-gradient-to-r from-gray-600 via-slate-500 white'>
            <div className=''>
                <h1 className='text-2xl font-serif font-medium text-gray-300'>Add Category</h1>
            </div>
            <form onSubmit={handleSubmit(set_category)} className='flex flex-col gap-2'>

                <input type="text" className='p-2 w-44 rounded-lg' placeholder='Python' {...register("category_name", { required: true })} />

                <textarea className='p-2 w-2/5 rounded-lg' placeholder='Write your thought here...' rows={5}
                    {...register("category_description", { required: true })}></textarea>

                <div className='w-36'>
                    <Button buttonType='submit'>
                        Add Category
                    </Button>
                </div>
                 {error? <p className='text-red-500 font-medium '>{error}</p>: ""} 
            </form>
        </main>
    )
}

export default Category