import React from 'react'

const Button = ({ children, buttonType }: {
    children: React.ReactNode,
    buttonType: "reset" | "submit" | "button"
}) => {
    
    return (
        <div className='w-full'>
            <button type={buttonType} className='w-full p-2 bg-black hover:bg-sky-800 text-white rounded-md'>
                {children}
            </button>
        </div>
    )
}

export default Button