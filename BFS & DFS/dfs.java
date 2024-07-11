import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class DFSExample {

    public static void main(String[] args) {
        Map<String, List<String>> graph = new HashMap<>();
        graph.put("A", new ArrayList<String>(List.of("B", "C")));
        graph.put("B", new ArrayList<String>(List.of("D", "E")));
        graph.put("C", new ArrayList<String>(List.of("F")));
        graph.put("D", new ArrayList<>());
        graph.put("E", new ArrayList<String>(List.of("F")));
        graph.put("F", new ArrayList<>());

        Set<String> visited = new HashSet<>();
        dfs(graph, "D", visited);
    }

    public static void dfs(Map<String, List<String>> graph, String start, Set<String> visited) {
        visited.add(start);
        System.out.println(start);

        for (String neighbor : graph.get(start)) {
            if (!visited.contains(neighbor)) {
                dfs(graph, neighbor, visited);
            }
        }
    }
}
