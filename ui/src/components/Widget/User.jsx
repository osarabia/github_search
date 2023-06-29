import "./widget.css"

export const User = ({data}) => {
    return (
        <>
            <section key={data['id']} className="widget">
                <a href={data['profile_picture']} target="_blank">Profile Picture</a>
                <p>name: {data['name']}</p>
                <p>location: {data['location']}</p>
            </section>
        </>
    );
}