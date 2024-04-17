import React from 'react'

const Button = ({ children, buttonType }: {
    children: React.ReactNode,
    buttonType: "reset" | "submit" | "button"
}) => {
    
    return (
        <div>
            <button type={buttonType} className='p-2 bg-sky-950 hover:bg-sky-800 text-white rounded-md'>
                {children}
            </button>
        </div>
    )
}

export default Button