import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import data as d
import sqlite3
db_name='YoutuberDB.db'
conn = sqlite3.connect(db_name)
cur=conn.cursor()
headers=['Youtuber','TotalGrade','SubscriberRank','VideoViewRank','Social Blade Rank','Estimated Year Earnings','Channel Type']

#Logic for picking the right app to Run
def sort(logic):
    if logic[0].lower()=='bar':
        if logic[1].lower()=='totalsubs':
            dat=d.get_data('subs')
            traces = []
            for item in dat:
                trace= go.Bar(
                    x=['Subscriber Total'],
                    y=[item[1]],
                    name=item[0]
                )
                traces.append(trace)
            layout = go.Layout(
                barmode='group'
            )
            fig = go.Figure(data=traces, layout=layout)

            trace = go.Table(
                header=dict(values=headers),
                cells=dict(values=[[tup[0]for tup in d.get_table_data()],
                    [tup[1]for tup in d.get_table_data()],
                    [tup[2]for tup in d.get_table_data()],
                    [tup[3]for tup in d.get_table_data()],
                    [tup[4]for tup in d.get_table_data()],
                    [tup[5]for tup in d.get_table_data()],
                    [tup[6]for tup in d.get_table_data()]
                    ])
                )

            data = [trace]
            table_fig=go.Figure(data=data)


            app_bar.layout = html.Div(children=[
                html.H1(children='Youtube Analyzer'),

                html.Div(children='''
                    Subscribers: Bar graph comparison of Youtuber Total Subscribers
                '''),
                dcc.Graph(
                    id='example-graph',
                    figure=fig),
                dcc.Graph(
                    id='Table',
                    figure=table_fig)
            ])
            return app_bar.layout
        elif logic[1].lower()=='totalviews':
            dat=d.get_data('views')
            traces = []
            for item in dat:
                trace= go.Bar(
                    x=['Views Total'],
                    y=[item[1]],
                    name=item[0]
                )
                traces.append(trace)
            layout = go.Layout(
                barmode='group'
            )
            fig = go.Figure(data=traces, layout=layout)
            trace = go.Table(
                header=dict(values=headers),
                cells=dict(values=[[tup[0]for tup in d.get_table_data()],
                    [tup[1]for tup in d.get_table_data()],
                    [tup[2]for tup in d.get_table_data()],
                    [tup[3]for tup in d.get_table_data()],
                    [tup[4]for tup in d.get_table_data()],
                    [tup[5]for tup in d.get_table_data()],
                    [tup[6]for tup in d.get_table_data()]
                    ])
                )

            data = [trace]
            table_fig=go.Figure(data=data)
            app_bar.layout = html.Div(children=[
                html.H1(children='Youtube Analyzer'),

                html.Div(children='''
                    Total Video Views: Bar graph comparison of Youtuber Total Channel Views
                '''),

                dcc.Graph(
                    id='example-graph',
                    figure=fig),
                dcc.Graph(
                    id='Table',
                    figure=table_fig)])
            return app_bar.layout
        elif logic[1].lower()=='totalview30':
            dat=d.get_data('ViewsLastThirty')
            traces = []
            for item in dat:
                trace= go.Bar(
                    x=['Views in the Last 30 days'],
                    y=[item[1]],
                    name=item[0]
                )
                traces.append(trace)
            layout = go.Layout(
                barmode='group'
            )
            fig = go.Figure(data=traces, layout=layout)
            trace = go.Table(
                header=dict(values=headers),
                cells=dict(values=[[tup[0]for tup in d.get_table_data()],
                    [tup[1]for tup in d.get_table_data()],
                    [tup[2]for tup in d.get_table_data()],
                    [tup[3]for tup in d.get_table_data()],
                    [tup[4]for tup in d.get_table_data()],
                    [tup[5]for tup in d.get_table_data()],
                    [tup[6]for tup in d.get_table_data()]
                    ])
                )

            data = [trace]
            table_fig=go.Figure(data=data)
            app_bar.layout = html.Div(children=[
                html.H1(children='Youtube Analyzer'),

                html.Div(children='''
                    Views in the Last 30 Days: Bar graph comparison of Video Views in the Last 30 days
                '''),

                dcc.Graph(
                    id='example-graph',
                    figure=fig),
                dcc.Graph(
                    id='Table',
                    figure=table_fig)
                 
                ])
            return app_bar.layout
        elif logic[1].lower()=='totalsubs30':
            dat=d.get_data('SubsLastThirty')
            traces = []
            for item in dat:
                trace= go.Bar(
                    x=['Subscribers Gained in the Last 30 days'],
                    y=[item[1]],
                    name=item[0]
                )
                traces.append(trace)
            layout = go.Layout(
                barmode='group'
            )
            fig = go.Figure(data=traces, layout=layout)
            trace = go.Table(
                header=dict(values=headers),
                cells=dict(values=[[tup[0]for tup in d.get_table_data()],
                    [tup[1]for tup in d.get_table_data()],
                    [tup[2]for tup in d.get_table_data()],
                    [tup[3]for tup in d.get_table_data()],
                    [tup[4]for tup in d.get_table_data()],
                    [tup[5]for tup in d.get_table_data()],
                    [tup[6]for tup in d.get_table_data()]
                    ])
                )

            data = [trace]
            table_fig=go.Figure(data=data)
            app_bar.layout = html.Div(children=[
                html.H1(children='Youtube Analyzer'),

                html.Div(children='''
                    Subscribers: Bar graph comparison of Youtuber Total Subscribers Gained in the Last 30 days
                '''),

                dcc.Graph(
                    id='example-graph',
                    figure=fig),
                dcc.Graph(
                    id='Table',
                    figure=table_fig)
                
                ])
            return app_bar.layout
        else:
            return False

    elif logic[0].lower()=='box':
        if logic[1].lower()=='twitter':
            d_twitter=d.get_data('twitter')
            traces = []
            for items in d_twitter[0]:
                data_points=[]
                for points in items[0]:
                    data_points.append(points[1])
                trace= go.Box(x=data_points, name=items[1])
                traces.append(trace)
            fig = go.Figure(data=traces)

            app_box.layout = html.Div(children=[
                html.H1(children='Youtube Analyzer'),

                html.Div(children='''
                    Twitter: Box Plot comparison of Twitter Senitment Analysis
                '''),

                dcc.Graph(
                    id='example-graph',
                    figure=fig),
                html.Div(children='''
                    Lowest Scoring Tweet: {} (In Reference to: {} Sentiment Score: {})
                    '''.format(d_twitter[1][0],d_twitter[1][1],d_twitter[1][2])),

                html.Div(children='''
                    Highest Scoring Tweet: {} (In Reference to: {} Sentiment Score: {})
                    '''.format(d_twitter[2][0],d_twitter[2][1],d_twitter[2][2]))
                ])
            return app_box.layout

        elif logic[1].lower()=='comments':
            d_comments=d.get_data('comments')
            traces = []
            for items in d_comments[0]:
                data_points=[]
                for points in items[0]:
                    data_points.append(points[1])
                trace= go.Box(x=data_points, name=items[1])
                traces.append(trace)
            fig = go.Figure(data=traces)
            app_box.layout = html.Div(children=[
                html.H1(children='Youtube Analyzer'),
                html.Div(children='''
                    Comments: Box Plot comparison of Youtube Comment Senitment Analysis
                '''),
                dcc.Graph(
                    id='example-graph',
                    figure=fig),
                html.Div(children='''
                    Lowest Scoring Comment: {} (In Reference to: {} Sentiment Score: {})
                    '''.format(d_comments[1][0],d_comments[1][1],d_comments[1][2])),

                html.Div(children='''
                    Highest Scoring Comment: {} (In Reference to: {} Sentiment Score: {})
                    '''.format(d_comments[2][0],d_comments[2][1],d_comments[2][2]))
                ])
            return app_box.layout

        else:
            return False

#Dash Application calls
app_bar = dash.Dash()
app_box = dash.Dash()

#Loads help text
def load_help_text():
    with open('help.txt') as f:
        return f.read()

#main
def main():
    help_text = load_help_text()
    print('Welcome to the Youtube Analyzer Application!\n')
    ipt=input('Please enter a command or type "help" for more information: ')
    while(ipt!='quit'):
        logic=ipt.split()
        if logic[0]=='bar':
            lay=sort(logic)
            if lay==False:
                ipt=input('Sorry,Command Not recognized, Please try agian:')
            else:
                app_bar.run_server()
                ipt=input('\nPlease enter a command or type "help" for more information: ')
        elif logic[0]=='box':
            lay=sort(logic)
            if lay==False:
                ipt=input('Sorry,Command Not recognized, Please try agian:')
            else:
                app_box.run_server()
                ipt=input('\nPlease enter a command or type "help" for more information: ')
        elif logic[0] == 'help':
            print(help_text)
            ipt=input('\nPlease enter a command or type "help" for more information: ')
        else:
            ipt=input('Sorry,Command Not recognized, Please try agian:')


if __name__ == '__main__':
    main()
    print("Bye!")
    
        

