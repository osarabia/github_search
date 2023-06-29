import "./widget.css"

export const Issue = ({data}) => {
    return (
        <>
            <section key={data['id']} className="widget">
                <p>title: {data['issue_title']}</p>
                <a href={data['issue_url']} target="_blank">url</a>
                <p>state: {data['state']}</p>
            </section>
        </>
    );
}