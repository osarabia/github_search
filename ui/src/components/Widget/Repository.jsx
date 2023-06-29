import "./widget.css"

export const Repository = ({data}) => {
    return (
        <>
            <section key={data['id']} className="widget">
                <p>name: {data['name']}</p>
                <p>author: {data['owner']}</p>
                <p>starts: {data['starts']}</p>
            </section>
        </>
    );
}