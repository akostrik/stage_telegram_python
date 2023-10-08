<template>
  <div class="landing">
    <h1>Welcome to the Dashboard</h1>
    <button @click="navigate('recordEditor')">Go to Record Editor</button>
    <button @click="navigate('binaryEditor')">Go to Binary Affirmations Editor</button>

    <input v-model="channelId" placeholder="Enter channel ID" />
    <button @click="saveChannel">Save Channel</button>

    <div id="cy" class="cytoscape-container"></div>
  </div>
</template>

<script>
import cytoscape from 'cytoscape';
import axios from 'axios';

export default {
  name: 'LandingPage',
  data() {
    return {
      channelId: '',
      chart: null,
      datacollection: {
        labels: [],
        datasets: [{
          label: 'Relations',
          data: [],
          borderColor: "#3e95cd",
          fill: false
        }]
      }
    };
  },
    mounted() {
    axios.get('http://localhost:3001/relations/').then(response => {
      const elements = [];

      response.data.forEach(relation => {
        // Add nodes for channels
        elements.push({ data: { id: relation.channel_a } });
        elements.push({ data: { id: relation.channel_b } });
        
        // Add edges between channels
        elements.push({
          data: {
            id: relation.channel_a + '-' + relation.channel_b,
            source: relation.channel_a,
            target: relation.channel_b,
            relation: relation.relation // This assumes relation is a numerical value indicating the strength or number of attachments.
          }
        });
      });

      // Initialize Cytoscape
      cytoscape({
        container: document.getElementById('cy'),
        elements: elements,
        style: [
          {
            selector: 'node',
            style: {
              label: 'data(id)'
            }
          },
          {
            selector: 'edge',
            style: {
              'curve-style': 'bezier',
              'width': 'data(relation)', // This will set the edge width based on the relation value.
              'label': 'data(relation)', // This will display the relation value as a label on the edge.
              'text-rotation': 'autorotate', // This rotates the text so it's aligned with the edge.
              'text-margin-y': -10 // This offsets the text a bit from the edge to make it more readable.
            }
          }
        ],
        layout: {
          name: 'cose' // This is a force-directed layout.
        }
      });
    });
  },
  methods: {
    navigate(route) {
      this.$emit('changeRoute', route);
    },
    async saveChannel() {
      try {
        const response = await axios.post('http://localhost:3001/saveChannel/', {
          channelId: this.channelId
        });
        
        if(response.data.success) {
          alert('Channel saved successfully!');
          this.channelId = '';
        } else {
          alert('Error saving channel');
        }
      } catch (error) {
        alert('Error saving channel');
      }
    },
    createChart() {
      const ctx = this.$refs.canvas.getContext('2d');
      this.chart = new Chart(ctx, {
        type: 'line',
        data: this.datacollection,
        options: { responsive: true, maintainAspectRatio: false }
      });
    }
  }
};
</script>

<style scoped>
.landing {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.chart {
  width: 80%;
  height: 400px;
  margin-top: 20px;
}


</style>

<style scoped>
.cytoscape-container {
  width: 80%;
  height: 400px;
  margin-top: 20px;
  border: 1px solid #aaa;
}
</style>
